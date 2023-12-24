import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()