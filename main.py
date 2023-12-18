  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)