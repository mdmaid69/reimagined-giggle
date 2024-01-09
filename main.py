import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()