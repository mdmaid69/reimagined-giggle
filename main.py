n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)