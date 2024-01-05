  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)