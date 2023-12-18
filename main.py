import array
def extend_array(array, iterable):
        array.extend(iterable)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)