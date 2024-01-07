import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()