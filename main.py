  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)