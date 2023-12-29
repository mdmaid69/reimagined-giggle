import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def reverse_array(array):
        array.reverse()