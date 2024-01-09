import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))