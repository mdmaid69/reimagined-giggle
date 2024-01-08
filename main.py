import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height