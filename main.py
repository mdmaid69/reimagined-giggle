import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()