import array
def get_list_from_array(array):
        return array.tolist()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)