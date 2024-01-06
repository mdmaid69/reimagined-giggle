text = "Hello, world!"
print("Reversed:", text[::-1])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)