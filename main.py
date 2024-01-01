import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)