import array
def get_array_as_bool(array):
        return bool(array)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)