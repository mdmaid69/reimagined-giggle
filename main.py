import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"