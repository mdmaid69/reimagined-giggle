import array
def clear_array(array):
        array *= 0
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)