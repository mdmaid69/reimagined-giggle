import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_area(radius):
        return 3.14 * radius * radius