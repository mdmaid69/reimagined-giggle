import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)