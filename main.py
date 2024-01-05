import array
def convert_array_to_list(array):
        return array.tolist()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)