import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)