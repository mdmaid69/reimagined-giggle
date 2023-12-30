import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def remove_from_array(array, item):
        array.remove(item)