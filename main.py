import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
x = 10
y = 20
print("Sum:", x + y)