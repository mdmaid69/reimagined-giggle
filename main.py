import sys
def add_to_python_path(path):
        sys.path.append(path)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()