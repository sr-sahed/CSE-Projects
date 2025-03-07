import os
import subprocess

print(os.getcwd())  # Current working directory

subprocess.run(["echo", "Hello from subprocess!"])
