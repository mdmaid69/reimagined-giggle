  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)