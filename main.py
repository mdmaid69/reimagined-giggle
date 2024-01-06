import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())