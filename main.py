  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)