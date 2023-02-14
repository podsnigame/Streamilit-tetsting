import streamlit as st
import os
import pdfminer.high_level
from pdf2image import convert_from_path
import pytesseract

st.title("PDF to Text Converter")

# Upload file
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Save uploaded file to temporary directory
    with open(os.path.join("temp", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Convert PDF to image
    images = convert_from_path(os.path.join("temp", uploaded_file.name))

    # Convert image to text using pytesseract
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)

    # Save text to temporary file
    with open(os.path.join("temp", "output.txt"), "w") as f:
        f.write(text)

    # Display text to user
    st.text_area("Converted Text", text)
