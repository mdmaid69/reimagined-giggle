import array
def pop_from_array(array, i=-1):
        return array.pop(i)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)