  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)