import time
def get_current_time():
        return time.time()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)