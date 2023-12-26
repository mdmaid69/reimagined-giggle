import collections
def create_counter():
        return collections.Counter()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)