import json
def convert_to_json(data):
        return json.dumps(data)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()