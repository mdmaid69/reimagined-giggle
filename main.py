def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)