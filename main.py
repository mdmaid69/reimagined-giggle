import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)