import array
def get_array_from_bytes(bytes, typecode):
        a = array.array(typecode)
        a.frombytes(bytes)
        return a
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)