  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)