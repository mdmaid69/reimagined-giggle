  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import json
def read_from_json(json_string):
        return json.loads(json_string)