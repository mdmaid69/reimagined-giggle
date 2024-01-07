import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time