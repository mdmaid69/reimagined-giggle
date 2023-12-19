import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_logarithm_base_10(x):
        return math.log10(x)