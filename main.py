  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)