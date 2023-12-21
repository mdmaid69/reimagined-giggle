import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)