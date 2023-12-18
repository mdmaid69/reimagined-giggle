import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)