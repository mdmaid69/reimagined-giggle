import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)