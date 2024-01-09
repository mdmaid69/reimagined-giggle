import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)