import random
print(random.randint(0, 100))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)