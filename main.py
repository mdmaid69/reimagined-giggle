  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)