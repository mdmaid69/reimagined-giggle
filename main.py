import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
for i in range(10): print(i)