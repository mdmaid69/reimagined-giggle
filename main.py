import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)