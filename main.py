  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()