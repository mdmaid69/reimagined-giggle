import array
def get_array_itemsize(array):
        return array.itemsize
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)