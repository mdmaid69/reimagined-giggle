import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def find_max(lst):
        return max(lst)