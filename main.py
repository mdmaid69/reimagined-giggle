import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
i = 0
while i < 5:
        print(i)
        i += 1