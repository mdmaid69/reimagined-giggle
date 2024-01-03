import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def add_numbers(x, y):
        return x + y