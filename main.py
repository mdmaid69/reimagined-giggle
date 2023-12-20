import array
def check_if_array_contains_item(array, item):
        return item in array
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)