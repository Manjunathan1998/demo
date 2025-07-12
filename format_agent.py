from openai import OpenAI
import os

# Create a client using the new SDK format
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get the content of main.py
with open("main.py", "r") as f:
    code = f.read()

# Send request to GPT-4 (or use "gpt-3.5-turbo" if needed)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code refactoring agent. Improve Pylint score and follow PEP8."},
        {"role": "user", "content": f"Refactor this code:\n\n{code}"}
    ],
    temperature=0.2
)

# Extract and save the improved code
refactored_code = response.choices[0].message.content

with open("main.py", "w") as f:
    f.write(refactored_code)

print("✅ Refactored code saved to main.py")