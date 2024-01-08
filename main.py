import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)