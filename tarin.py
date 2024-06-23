import torch
from transformers import BartTokenizer, BartForConditionalGeneration, Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset
import os
import re

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load the CNN/Daily Mail dataset
dataset = load_dataset('cnn_dailymail', '3.0.0')

# Tokenizer and model setup
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

# Preprocessing function
def preprocess_function(examples):
    inputs = [doc for doc in examples['article']]
    model_inputs = tokenizer(inputs, max_length=1024, truncation=True, padding='max_length')
    
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples['highlights'], max_length=128, truncation=True, padding='max_length')
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

# Apply preprocessing
tokenized_datasets = dataset.map(preprocess_function, batched=True, remove_columns=['article', 'highlights', 'id'])

# Data collator for padding
data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

from torch.utils.data import DataLoader

train_dataloader = DataLoader(tokenized_datasets['train'], batch_size=4, collate_fn=data_collator)
eval_dataloader = DataLoader(tokenized_datasets['validation'], batch_size=4, collate_fn=data_collator)

from transformers import TrainingArguments, Trainer

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
    push_to_hub=False,
    save_steps=10000,
    save_total_limit=2
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets['train'],
    eval_dataset=tokenized_datasets['validation'],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Function to find the latest checkpoint
def get_latest_checkpoint(output_dir):
    checkpoints = [d for d in os.listdir(output_dir) if re.match(r'checkpoint-\d+', d)]
    if not checkpoints:
        return None
    latest_checkpoint = max(checkpoints, key=lambda x: int(x.split('-')[-1]))
    return os.path.join(output_dir, latest_checkpoint)

# Path to the results directory
output_dir = './results'

# Get the latest checkpoint
latest_checkpoint = get_latest_checkpoint(output_dir)

# Start training, resuming from checkpoint if it exists
if latest_checkpoint:
    print(f"Resuming training from checkpoint: {latest_checkpoint}")
    trainer.train(resume_from_checkpoint=latest_checkpoint)
else:
    print("No checkpoint found. Starting training from scratch.")
    trainer.train()

# Save the final model
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
