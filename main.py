import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use the correct available model
model = genai.GenerativeModel("models/gemini-1.5-flash")

def solve_math_problem(question):
    prompt = f"""
You are a helpful math tutor. Solve this problem step-by-step:

Problem: {question}

Explain clearly, and give the final answer at the end.
"""
    response = model.generate_content([prompt])
    return response.text


