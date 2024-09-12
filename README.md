

# Blog Generation Platform

This project generates blog content using the LLama 2 language model, integrated with a Flask-based web interface.

## Features
- Generate blog posts based on topic, word count, and writing style.
- Customizable blog styles (e.g., casual, formal).
- AI-driven content using LLama 2 model.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/AkashKobal/Blog-Generation-Platform.git
cd Blog-Generation-Platform
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install langchain langchain_community ctransformers Flask
```

### 4. Download LLama 2 Model
Download the LLama 2 model on Huggingface(https://huggingface.co/localmodels/Llama-2-7B-Chat-ggml/tree/main) and place it in the `models/llama2/` directory.

### 5. Run the Flask App
```bash
python app.py
```

Access the app at `http://localhost:5000`.

## Requirements
- Python 3.7+
- Flask
- Langchain


