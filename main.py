def calculate_average(lst):
        return sum(lst) / len(lst)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)