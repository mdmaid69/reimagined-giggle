  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()