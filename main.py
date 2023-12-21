  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)