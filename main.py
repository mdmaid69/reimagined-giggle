def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)