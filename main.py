import array
def get_array_as_bytes(array):
        return bytes(array)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)