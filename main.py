import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()