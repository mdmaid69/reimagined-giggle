def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)