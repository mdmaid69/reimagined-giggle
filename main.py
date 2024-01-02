import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))