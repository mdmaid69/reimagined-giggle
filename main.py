  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)