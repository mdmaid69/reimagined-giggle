def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)