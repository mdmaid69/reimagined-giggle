  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)