  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)