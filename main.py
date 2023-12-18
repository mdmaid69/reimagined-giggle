import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def convert_to_octal(n):
        return oct(n)