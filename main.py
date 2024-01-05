import datetime
def get_current_datetime():
        return datetime.datetime.now()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)