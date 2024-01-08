  import os
  def delete_file(file_name):
        os.remove(file_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()