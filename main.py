n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)