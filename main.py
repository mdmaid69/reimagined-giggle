import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)