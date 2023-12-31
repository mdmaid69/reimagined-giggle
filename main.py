import array
def iterate_over_array(array):
        for item in array:
        print(item)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)