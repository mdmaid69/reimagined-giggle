  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value