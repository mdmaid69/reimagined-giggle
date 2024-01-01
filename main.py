import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()