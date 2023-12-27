import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)