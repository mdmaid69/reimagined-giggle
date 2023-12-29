import math
def calculate_sphere_volume(radius):
        return 4/3 * math.pi * radius**3
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)