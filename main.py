  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)