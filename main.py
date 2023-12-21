import array
def set_array_item(array, i, item):
        array[i] = item
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)