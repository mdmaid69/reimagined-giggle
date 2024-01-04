  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())