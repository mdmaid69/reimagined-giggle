import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)