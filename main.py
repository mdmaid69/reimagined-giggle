  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)