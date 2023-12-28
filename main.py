import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()