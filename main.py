import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)