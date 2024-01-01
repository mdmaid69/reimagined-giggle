  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import glob
def find_files(pattern):
        return glob.glob(pattern)