import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def append_to_array(array, item):
        array.append(item)