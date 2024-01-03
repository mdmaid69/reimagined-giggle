import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable