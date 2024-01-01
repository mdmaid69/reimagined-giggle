import time
def get_current_time():
        return time.ctime()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)