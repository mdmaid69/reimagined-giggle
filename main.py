import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)