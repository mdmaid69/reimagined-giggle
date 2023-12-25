  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)