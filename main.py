import collections
def create_queue():
        return collections.deque()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)