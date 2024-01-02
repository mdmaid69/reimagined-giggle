  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)