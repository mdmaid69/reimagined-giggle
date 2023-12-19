def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)