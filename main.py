import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)