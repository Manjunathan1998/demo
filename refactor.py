import os
import subprocess
import openai

# 1. Read the code
with open("main.py", "r") as f:
    code = f.read()

# 2. Use OpenAI to refactor the code (e.g., fix style/lint)
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful code formatter. Improve the Pylint score of the code."},
        {"role": "user", "content": f"Refactor this Python code to improve Pylint score:\n\n{code}"}
    ]
)

refactored_code = response['choices'][0]['message']['content']

# 3. Overwrite file
with open("main.py", "w") as f:
    f.write(refactored_code)

# 4. Commit and push changes (requires GitHub token)
subprocess.run("git config user.name github-actions", shell=True)
subprocess.run("git config user.email github-actions@github.com", shell=True)
subprocess.run("git add main.py", shell=True)
subprocess.run("git commit -m 'fix: auto-refactor via agentic AI to improve pylint score'", shell=True)
subprocess.run("git push", shell=True)
