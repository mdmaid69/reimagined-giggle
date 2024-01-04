import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_area_triangle(b, h):
        return 0.5 * b * h