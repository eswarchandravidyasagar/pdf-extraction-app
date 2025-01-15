import fitz  # PyMuPDF
import openai
import os
import hashlib
import json

cache = {}

# Function to extract text from PDF using PyMuPDF
def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to preprocess and clean extracted text
def preprocess_text(text):
    # Example preprocessing steps
    text = text.replace('\n', ' ')
    text = ' '.join(text.split())
    return text

# Function to use GPT-4 to identify and extract specific data points
def extract_data_points(text, prompt=None):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if prompt:
        full_prompt = f"{prompt}: {text}"
    else:
        full_prompt = f"Extract specific data points from the following text: {text}"
    
    # Create a unique hash for the prompt to use as a cache key
    cache_key = hashlib.md5(full_prompt.encode()).hexdigest()
    
    # Check if the result is already in the cache
    if cache_key in cache:
        return cache[cache_key]
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=full_prompt,
        max_tokens=1000
    )
    result = response.choices[0].text.strip()
    
    # Store the result in the cache
    cache[cache_key] = result
    
    return result
