  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)