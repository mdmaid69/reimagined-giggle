  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()