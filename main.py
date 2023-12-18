import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_sine(x):
        return math.sin(x)