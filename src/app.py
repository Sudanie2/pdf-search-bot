import streamlit as st
from download_pdf import download_pdf
from extract_text import extract_text_from_pdf
from ask_gemini import ask_gemini

st.title("📄 PDF検索チャットボット")

# GCSからPDFを取得
pdf_file = download_pdf()
pdf_text = extract_text_from_pdf(pdf_file)

query = st.text_input("質問を入力してください:")

if query:
    answer = ask_gemini(query, pdf_text)
    st.write("### 🤖 Geminiの回答")
    st.write(answer)
