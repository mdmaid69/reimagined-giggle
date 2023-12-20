  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()