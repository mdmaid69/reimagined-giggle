  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)