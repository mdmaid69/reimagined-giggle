import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))