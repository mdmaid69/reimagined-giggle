import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))