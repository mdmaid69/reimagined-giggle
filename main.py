import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def sort_list(lst):
        return sorted(lst)