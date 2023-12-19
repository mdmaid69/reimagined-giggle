name = "Python"
print("Hello,", name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)