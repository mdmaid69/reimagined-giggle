import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)