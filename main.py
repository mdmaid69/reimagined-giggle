import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def calculate_roi(gain, cost):
        return (gain - cost) / cost