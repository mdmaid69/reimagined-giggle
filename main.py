import platform
def get_python_version():
        return platform.python_version()
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()