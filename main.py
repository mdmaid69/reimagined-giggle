  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()