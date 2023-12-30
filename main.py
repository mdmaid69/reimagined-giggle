import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  def cube_number(x):
        return x**3