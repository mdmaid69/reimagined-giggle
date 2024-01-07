import array
def get_string_from_array(array):
        return array.tobytes()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)