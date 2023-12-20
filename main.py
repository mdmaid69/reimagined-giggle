  import numpy as np
  def calculate_variance(arr):
        return np.var(arr)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)