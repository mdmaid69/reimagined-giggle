import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)