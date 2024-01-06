  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()