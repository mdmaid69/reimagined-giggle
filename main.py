  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import shutil
def move_file(src, dst):
        shutil.move(src, dst)