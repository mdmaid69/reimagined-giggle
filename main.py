text = "Hello, world!"
print("Uppercase:", text.upper())
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)