import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_perimeter_triangle(a, b, c):
        return a + b + c