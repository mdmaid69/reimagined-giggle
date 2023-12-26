  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)