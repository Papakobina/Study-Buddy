# Study-Buddy
# NLP Notes Summarizer and Flowchart Generator

## Overview
This project integrates advanced Natural Language Processing (NLP) techniques to summarize Notes, generates interactive flowcharts, and provide a question-answering interface based on the summarized text. The goal is to enhance the readability and usability of lengthy articles by providing concise summaries, visual representations, and interactive Q&A capabilities.

<img src='https://github.com/Papakobina/Study-Buddy/blob/main/Screenshot%202024-06-23%20021217.png'/>
<img src='https://github.com/Papakobina/Study-Buddy/blob/main/Screenshot%202024-06-23%20023204.png'/>

### Demo : https://www.youtube.com/watch?v=_uU9DPO6mBo

## Features
- **Article Summarization:** Automatically generate concise summaries of long articles using a fine-tuned BART model.
- **Flowchart Generation:** Visualize the content of articles as flowcharts using the Whimsical platform and Selenium automation.
- **Question Answering:** Allow users to ask questions about the summarized text using a pre-trained BERT model.

## Technology Stack
- **Python:** Core programming language used.
- **Streamlit:** For building an interactive web application.
- **Transformers (Hugging Face):** For state-of-the-art NLP models.
- **Selenium:** For browser automation to generate flowcharts.
- **pyautogui:** For simulating keyboard shortcuts.
- **Pillow:** For image handling and manipulation.
- **pyperclip:** For clipboard operations.

## Project Workflow

### 1. Training the Models

#### Article Summarization
- **Model:** BART (Bidirectional and Auto-Regressive Transformers)
- **Process:** 
  - The BART model was fine-tuned on a large dataset to understand and generate summaries of text.
  - Fine-tuning involved training the BART model on the CNN/Daily Mail dataset, which is widely used for text summarization tasks.

#### Question Answering
- **Model:** BERT (Bidirectional Encoder Representations from Transformers)
- **Process:** 
  - The BERT model, pre-trained on the SQuAD (Stanford Question Answering Dataset), was used for the question-answering component.
  - This model allows extracting relevant answers from the summarized text based on user queries.

### 2. Application Development

#### Streamlit Interface
- Streamlit was chosen for its simplicity and rapid development capabilities to build the interactive web application.
- The app provides an interface for users to input articles, view summaries, and interact with the Q&A system.

#### Flowchart Generation
- Selenium was used to automate browser actions on Whimsical, a web-based tool for creating flowcharts.
- The script logs into Whimsical, creates a new board, generates a mind map using the summarized text, and captures the flowchart as an image.

### 3. Integration and Deployment
- The summarized text is passed to the Whimsical automation script to generate the flowchart.
- The flowchart image is then displayed on the Streamlit interface alongside the text summary and Q&A functionality.

## Technical Explanation

### Summarization
- **Model:** BART (Bidirectional and Auto-Regressive Transformers)
- **Process:** 
  - The input article is tokenized using the BART tokenizer.
  - The tokenized text is fed into the fine-tuned BART model to generate a summary.
  - The summary is displayed to the user in the Streamlit interface.

### Flowchart Generation
- **Automation Tool:** Selenium
- **Process:** 
  - Selenium opens a headless Chrome browser and navigates to the Whimsical website.
  - It logs into the user account and creates a new board.
  - The summarized text is entered into the mind map generator.
  - A flowchart is generated and copied as an image using simulated keyboard shortcuts.
  - The image is saved and displayed in the Streamlit interface.

### Question Answering
- **Model:** BERT (Bidirectional Encoder Representations from Transformers)
- **Process:** 
  - The summarized text is used as context for the BERT question-answering pipeline.
  - User questions are tokenized and processed by the BERT model to extract relevant answers from the context.
  - The answers are displayed in the Streamlit interface.
