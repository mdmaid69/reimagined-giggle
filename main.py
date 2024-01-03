import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)