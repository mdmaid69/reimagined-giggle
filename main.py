  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)