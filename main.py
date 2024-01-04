  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)