import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
from collections import Counter
print(Counter("hello world"))