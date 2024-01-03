  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)