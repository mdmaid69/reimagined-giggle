import math
def calculate_logarithm_of_gamma_function(x):
        return math.lgamma(x)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)