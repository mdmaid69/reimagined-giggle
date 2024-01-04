  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import json
def convert_to_json(data):
        return json.dumps(data)