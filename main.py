  import os
  def get_base_name(path):
        return os.path.basename(path)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)