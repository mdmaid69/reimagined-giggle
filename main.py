import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()