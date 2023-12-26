  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)