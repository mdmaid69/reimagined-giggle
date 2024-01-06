import datetime
def get_today_date():
        return datetime.date.today()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)