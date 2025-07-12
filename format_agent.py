import openai
import os

# Load API key securely
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("❌ OPENAI_API_KEY is missing!")

openai.api_key = api_key

# Read the code from main.py
with open("main.py", "r") as f:
    code = f.read()

# Call GPT-4 to refactor the code
response = openai.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Refactor and reformat this Python code to follow PEP8 and improve Pylint score."},
        {"role": "user", "content": code}
    ],
    temperature=0.3
)

# Get the refactored code
refactored_code = response.choices[0].message.content

# Save the updated code
with open("main.py", "w") as f:
    f.write(refactored_code)

print("✅ Code refactored and saved to main.py")
