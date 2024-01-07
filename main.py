import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))