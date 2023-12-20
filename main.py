import math
def calculate_greatest_common_divisor(a, b):
        return math.gcd(a, b)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)