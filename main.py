n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)