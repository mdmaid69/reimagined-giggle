  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()