import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)