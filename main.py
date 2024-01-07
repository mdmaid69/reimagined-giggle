  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)