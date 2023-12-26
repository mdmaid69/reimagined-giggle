import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)