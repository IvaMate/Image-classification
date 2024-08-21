#from dotenv import find_dotenv, load_dotenv #pip install python-dotenv
from transformers import pipeline
import streamlit as st
from PIL import Image

#chose a model
pipeline = pipeline(task="image-classification", model="./model/checkpoint-334")


st.title("Image classification")

file_name = st.file_uploader("Upload an image")

if file_name is not None:
    col1, col2 = st.columns(2)

    image = Image.open(file_name)
    col1.image(image, use_column_width=True)
    predictions = pipeline(image)

    col2.header("Probabilities")
    for p in predictions:
        col2.subheader(f"{ p['label'] }: { round(p['score'] * 100, 1)}%")