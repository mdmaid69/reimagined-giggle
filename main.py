  def is_even(n):
        return n % 2 == 0
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)