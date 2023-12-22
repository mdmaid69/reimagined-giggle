def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)