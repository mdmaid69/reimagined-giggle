  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)