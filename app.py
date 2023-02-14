import streamlit as st
import PyPDF2
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="PDF/Image to Text Converter with OCR")

st.title("PDF/Image to Text Converter with OCR")

file = st.file_uploader("Upload file", type=["pdf", "png", "jpg", "jpeg"])
if file is not None:
  content = file.read()

  if file.type == "application/pdf":
    pdf_reader = PyPDF2.PdfFileReader(io.BytesIO(content))
    page = pdf_reader.getPage(0)
    text = page.extractText()
    st.write(text)

  else:
    img = Image.open(io.BytesIO(content))
    text = pytesseract.image_to_string(img)
    st.write(text)

  # Menyimpan hasil konversi sebagai file teks dan menampilkan tombol unduh
  if st.button("Download Text"):
    if file.type == "application/pdf":
      output_file = f"{file.name.split('.')[0]}.txt"
    else:
      output_file = f"{file.name.split('.')[0]}.txt"
    with open(output_file, "w") as f:
      f.write(text)
    st.download_button(label="Download Text",
                       data=io.BytesIO(text.encode("utf-8")).getvalue(),
                       file_name=output_file,
                       mime="text/plain")
