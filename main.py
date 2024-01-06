import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()