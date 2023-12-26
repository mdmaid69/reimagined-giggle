import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def delete_file(file_name):
        os.remove(file_name)