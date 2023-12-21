  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import json
def read_from_json(json_string):
        return json.loads(json_string)