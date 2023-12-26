import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()