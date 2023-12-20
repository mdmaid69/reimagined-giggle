  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()