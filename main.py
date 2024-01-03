import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)