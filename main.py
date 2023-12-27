import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))