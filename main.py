import array
def get_array_as_frozenset(array):
        return frozenset(array)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)