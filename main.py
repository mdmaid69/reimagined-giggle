import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import time
def get_time_since_epoch():
        return time.time()