import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()