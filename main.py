import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)