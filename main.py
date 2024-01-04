  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)