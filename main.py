n = 10
print("Square numbers:", [x**2 for x in range(n)])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)