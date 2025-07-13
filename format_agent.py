import subprocess

print("🔧 Running autopep8...")
subprocess.run(["autopep8", "--in-place", "--aggressive", "--aggressive", "main.py"])

print("🎨 Running black...")
subprocess.run(["black", "main.py"])

print("📦 Sorting imports...")
subprocess.run(["isort", "main.py"])

print("✅ Code auto-fixed.")