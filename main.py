  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()