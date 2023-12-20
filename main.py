import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)