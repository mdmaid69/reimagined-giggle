  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)