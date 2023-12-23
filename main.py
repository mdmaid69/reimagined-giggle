import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()