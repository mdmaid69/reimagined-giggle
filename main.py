import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()