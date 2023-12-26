import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()