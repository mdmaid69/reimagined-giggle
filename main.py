  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)