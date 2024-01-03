  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]