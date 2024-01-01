  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)