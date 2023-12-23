numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)