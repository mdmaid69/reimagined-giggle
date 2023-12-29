import array
def get_array_buffer_info(array):
        return array.buffer_info()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)