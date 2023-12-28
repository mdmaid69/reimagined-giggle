  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)