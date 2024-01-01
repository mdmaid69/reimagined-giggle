import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)