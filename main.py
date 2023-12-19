import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)