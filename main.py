print([x**2 for x in range(10)])
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)