import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import math
def calculate_circle_area(radius):
        return math.pi * radius**2