  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)