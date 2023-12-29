import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)