import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import datetime
print(datetime.datetime.now())