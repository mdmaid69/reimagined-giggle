  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import sys
def add_to_python_path(path):
        sys.path.append(path)