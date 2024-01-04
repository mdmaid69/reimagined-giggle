  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)