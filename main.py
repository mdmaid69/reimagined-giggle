import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def get_array_as_float(array):
        return float(array[0])