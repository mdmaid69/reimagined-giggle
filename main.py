import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns