import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)