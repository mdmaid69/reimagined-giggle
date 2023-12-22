import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()