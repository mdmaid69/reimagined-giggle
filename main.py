import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()