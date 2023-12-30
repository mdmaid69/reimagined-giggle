import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)