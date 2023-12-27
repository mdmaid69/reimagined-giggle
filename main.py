  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import shutil
def delete_directory(path):
        shutil.rmtree(path)