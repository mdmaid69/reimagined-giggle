import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import re
print(re.match("h.*o", "hello world"))