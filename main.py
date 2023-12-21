import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))