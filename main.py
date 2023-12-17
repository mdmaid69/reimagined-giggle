import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def get_current_directory():
        return os.getcwd()