import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_logarithm_base_e(x):
        return math.log(x)