import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_area_circle(r):
        return 3.14 * r**2