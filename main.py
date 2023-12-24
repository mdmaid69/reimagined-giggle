import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def split_path(path):
        return os.path.split(path)