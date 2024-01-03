import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue