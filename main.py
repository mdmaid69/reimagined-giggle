import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
n = 10
print("Powers of 2:", [2**x for x in range(n)])