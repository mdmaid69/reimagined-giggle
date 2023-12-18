  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import shutil
def delete_directory(path):
        shutil.rmtree(path)