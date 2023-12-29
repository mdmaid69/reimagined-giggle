  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)