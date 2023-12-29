  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import subprocess
def run_command(cmd):
        return subprocess.check_output(cmd, shell=True)