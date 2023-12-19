import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def greet(name):
        print(f"Hello, {name}!")