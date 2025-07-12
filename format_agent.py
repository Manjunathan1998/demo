from openai import OpenAI
import os

# Load OpenAI key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("❌ OPENAI_API_KEY is missing!")

client = OpenAI(api_key=api_key)

# Read code
with open("main.py", "r") as f:
    code = f.read()

# Call GPT-4 to refactor
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an AI assistant that refactors Python code to improve Pylint score and follow PEP8 style."},
        {"role": "user", "content": f"Refactor this code:\n\n{code}"}
    ],
    temperature=0.2
)

# Save refactored code
refactored = response.choices[0].message.content
with open("main.py", "w") as f:
    f.write(refactored)

print("✅ Code refactored and saved.")
