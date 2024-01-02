import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import numpy as np
print(np.array([1, 2, 3]))