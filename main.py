  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())