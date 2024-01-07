import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_hyperbolic_cosine(x):
        return math.cosh(x)