  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)