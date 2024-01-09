import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)