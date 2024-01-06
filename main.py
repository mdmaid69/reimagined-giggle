  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)