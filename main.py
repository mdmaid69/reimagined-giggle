import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
def is_palindrome(s):
        return s == s[::-1]