  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)