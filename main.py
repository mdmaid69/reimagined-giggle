  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)