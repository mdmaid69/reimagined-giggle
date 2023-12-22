  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()