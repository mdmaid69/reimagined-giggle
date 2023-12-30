import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import itertools
print(list(itertools.permutations([1, 2, 3])))