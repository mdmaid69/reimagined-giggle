import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import numpy as np
  def create_numpy_array(lst):
        return np.array(lst)