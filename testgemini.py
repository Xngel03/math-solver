import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyDKynSQMY8I5-DRdTpIHahbi4Ac0pPa4qE")

for m in genai.list_models():
    print(m.name)
