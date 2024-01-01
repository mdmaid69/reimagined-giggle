import shutil
def delete_directory(path):
        shutil.rmtree(path)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()