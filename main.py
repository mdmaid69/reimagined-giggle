  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h