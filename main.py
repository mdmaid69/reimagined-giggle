import platform
def get_os_info():
        return platform.uname()
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()