import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b