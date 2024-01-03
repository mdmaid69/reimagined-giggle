import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()