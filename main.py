import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)