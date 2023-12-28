  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)