  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()