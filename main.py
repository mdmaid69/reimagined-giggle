  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()