  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()