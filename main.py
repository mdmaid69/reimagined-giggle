import array
def insert_into_array(array, i, item):
        array.insert(i, item)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)