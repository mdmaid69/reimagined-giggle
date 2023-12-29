import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)