import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()