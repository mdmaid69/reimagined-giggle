import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import os
def get_environment_variable(var):
        return os.getenv(var)