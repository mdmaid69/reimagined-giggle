import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)