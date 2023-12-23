import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)