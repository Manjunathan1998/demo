from openai import OpenAI
import os

# Load API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("❌ OPENAI_API_KEY is missing!")

# Init OpenAI client
client = OpenAI(api_key=api_key)

# Read the code
with open("main.py", "r") as f:
    code = f.read()

# Call GPT-4 to refactor code
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Refactor the Python code to improve Pylint score and follow PEP8."},
        {"role": "user", "content": f"Refactor this code:\n\n{code}"}
    ],
    temperature=0.3
)

# Extract and overwrite main.py
refactored_code = response.choices[0].message.content

with open("main.py", "w") as f:
    f.write(refactored_code)

print("✅ Code refactored and saved to main.py")
