import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import platform
def get_os_info():
        return platform.uname()