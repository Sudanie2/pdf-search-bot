import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # .envを読み込む

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def ask_gemini(question, context):
    """Gemini API で回答を生成"""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"以下の内容をもとに質問に答えてください: {context}\n\n質問: {question}")
    return response.text
