def find_union(list1, list2):
        return set(list1) | set(list2)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)