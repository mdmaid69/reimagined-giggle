import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.python.org", 80))