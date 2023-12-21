import os
def get_environment_variable(var):
        return os.getenv(var)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()