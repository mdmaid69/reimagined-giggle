import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()