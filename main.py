import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)