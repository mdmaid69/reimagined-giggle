import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def add_numbers(a, b):
        return a + b