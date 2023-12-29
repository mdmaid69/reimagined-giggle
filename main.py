import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import datetime
def get_current_date():
        return datetime.date.today()