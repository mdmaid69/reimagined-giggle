  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)