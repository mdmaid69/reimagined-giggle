import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities