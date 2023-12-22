import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))