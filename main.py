def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)