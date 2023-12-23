import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)