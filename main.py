  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)