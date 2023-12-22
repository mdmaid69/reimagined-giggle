  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)