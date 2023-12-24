text = "Hello, world!"
print("Words:", len(text.split()))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)