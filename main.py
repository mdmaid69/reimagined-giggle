import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def reverse_list(lst):
        return lst[::-1]