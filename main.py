import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)