  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()