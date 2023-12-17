import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()