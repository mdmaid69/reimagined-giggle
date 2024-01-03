import math
def calculate_error_function(x):
        return math.erf(x)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)