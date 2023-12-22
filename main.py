import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)