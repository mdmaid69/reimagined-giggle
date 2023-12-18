import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_circumference_circle(r):
        return 2 * 3.14 * r