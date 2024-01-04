import math
def calculate_sign(x):
        return math.copysign(1, x)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)