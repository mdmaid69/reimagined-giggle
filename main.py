import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])