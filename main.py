  import numpy as np
  def calculate_correlation(arr1, arr2):
        return np.corrcoef(arr1, arr2)
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)