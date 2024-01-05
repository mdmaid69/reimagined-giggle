import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)