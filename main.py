import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def reverse_string(s):
        return s[::-1]