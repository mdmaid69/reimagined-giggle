import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()