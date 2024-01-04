import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)