import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()