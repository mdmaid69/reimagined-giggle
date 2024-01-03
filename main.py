  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()