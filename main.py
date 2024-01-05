import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()