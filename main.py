  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)