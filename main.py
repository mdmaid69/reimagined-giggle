  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)