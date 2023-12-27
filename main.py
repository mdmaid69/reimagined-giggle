import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)