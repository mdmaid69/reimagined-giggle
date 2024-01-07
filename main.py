  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)