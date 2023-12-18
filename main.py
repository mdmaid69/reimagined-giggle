  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)