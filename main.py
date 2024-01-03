import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)