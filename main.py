  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)