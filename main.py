import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)