  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)