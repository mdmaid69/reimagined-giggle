import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))