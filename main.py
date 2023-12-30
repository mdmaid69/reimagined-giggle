  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)