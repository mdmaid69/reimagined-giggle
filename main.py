import math
def calculate_factorial(n):
        return math.factorial(n)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)