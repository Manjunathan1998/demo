import openai
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("❌ OPENAI_API_KEY is missing!")

openai.api_key = api_key

with open("main.py", "r") as f:
    code = f.read()

response = openai.chat.completions.create(
    model="gpt-3.5-turbo",  # ✅ Use this model
    messages=[
        {"role": "system", "content": "Refactor this Python code to follow PEP8 and improve Pylint score."},
        {"role": "user", "content": code}
    ],
    temperature=0.3
)

refactored_code = response.choices[0].message.content

with open("main.py", "w") as f:
    f.write(refactored_code)

print("✅ Code refactored with gpt-3.5-turbo.")
