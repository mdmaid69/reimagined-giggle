import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)