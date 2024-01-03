  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)