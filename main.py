import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  def multiply_numbers(x, y):
        return x * y