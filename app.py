import streamlit as st
import pytesseract
from PIL import Image
import io

# Fungsi untuk mengonversi file PDF menjadi teks
def pdf_to_text(file):
    text = ""
    with open(file, "rb") as f:
        pdf = PyPDF2.PdfFileReader(f)
        for page_num in range(pdf.numPages):
            page = pdf.getPage(page_num)
            text += page.extractText()
    return text

# Fungsi untuk mengonversi gambar menjadi teks
def image_to_text(image):
    text = pytesseract.image_to_string(image)
    return text

st.title("Konversi PDF dan Gambar ke Teks")

# Pilihan jenis file
file_type = st.selectbox("Pilih jenis file", ["PDF", "Gambar"])

# Upload file
uploaded_file = st.file_uploader("Upload file", type=[file_type.lower()])

if uploaded_file is not None:
    if file_type == "PDF":
        text = pdf_to_text(uploaded_file)
    else:
        image = Image.open(io.BytesIO(uploaded_file.read()))
        text = image_to_text(image)
    st.write("Hasil konversi:")
    st.write(text)
