import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))