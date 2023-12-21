def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)