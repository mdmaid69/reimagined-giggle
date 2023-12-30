import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()