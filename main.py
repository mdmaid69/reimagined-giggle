  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)