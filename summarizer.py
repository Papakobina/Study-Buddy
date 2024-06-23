from transformers import BartTokenizer, BartForConditionalGeneration, pipeline, AutoTokenizer, AutoModelForQuestionAnswering
import streamlit as st
from get_flow_chart import get_mind_map
import time
import os

# Load the fine-tuned model and tokenizer for summarization
checkpoint_dir = './checkpoint-6000'
summarization_model = BartForConditionalGeneration.from_pretrained(checkpoint_dir)
summarization_tokenizer = BartTokenizer.from_pretrained(checkpoint_dir)
summarizer = pipeline('summarization', model=summarization_model, tokenizer=summarization_tokenizer)

# Load the model and tokenizer for question answering
qa_model_name = "google-bert/bert-large-uncased-whole-word-masking-finetuned-squad"
qa_tokenizer = AutoTokenizer.from_pretrained(qa_model_name)
qa_model = AutoModelForQuestionAnswering.from_pretrained(qa_model_name)
qa_pipeline = pipeline('question-answering', model=qa_model, tokenizer=qa_tokenizer)

# Streamlit app
st.title("Article Summarizer and Q&A")
user_input = st.text_area("Enter your article here:")

if st.button("Summarize"):
    
    
    with st.spinner('Generating the flowchart...'):
    # Display the flowchart
        flowchart_path = get_mind_map(user_input)
    if os.path.exists(flowchart_path):
        st.image(flowchart_path)
    else:
        st.write("Failed to generate flowchart.")
        
    # Generate summary
    with st.spinner('Summarizing the text...'):
        summary = summarizer(user_input, max_length=150, min_length=30, do_sample=False)
        summarized_text = summary[0]['summary_text']
        st.write("Summary:")
        st.write(summarized_text)
        
    
st.write("You can now ask questions about the summarized text below:")

# Get the question from the user
question = st.text_input("Enter your question here:")
    
if st.button("Get Answer"):
    if question:
        # Generate answer
        qa_input = {
            'question': question,
            'context': user_input
        }
        answer = qa_pipeline(qa_input)
        st.write("Answer:")
        st.write(answer['answer'])
    else:
        st.write("Please enter a question.")
  

    
    

