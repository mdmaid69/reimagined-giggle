  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()