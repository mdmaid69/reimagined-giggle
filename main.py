import re
def split_string(pattern, string):
        return re.split(pattern, string)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)