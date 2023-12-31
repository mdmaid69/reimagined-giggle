text = "Hello, world!"
print("Characters:", len(text))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)