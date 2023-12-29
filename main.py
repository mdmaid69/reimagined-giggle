  def remove_duplicates(lst):
        return list(set(lst))
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)