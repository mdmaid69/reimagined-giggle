  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)