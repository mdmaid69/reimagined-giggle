import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def convert_array_to_string(array):
        return array.tostring()