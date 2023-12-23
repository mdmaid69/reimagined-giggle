import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)