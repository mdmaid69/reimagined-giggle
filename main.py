import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"