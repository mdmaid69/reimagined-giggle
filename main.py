import collections
def create_stack():
        return collections.deque()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)