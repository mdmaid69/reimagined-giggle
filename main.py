import math
def calculate_absolute_value(x):
        return math.fabs(x)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)