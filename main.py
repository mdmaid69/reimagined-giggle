import array
def get_array_item(array, i):
        return array[i]
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)