import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def square_number(x):
        return x**2