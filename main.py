  import os
  def get_current_working_directory():
        return os.getcwd()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)