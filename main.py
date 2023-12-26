  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()