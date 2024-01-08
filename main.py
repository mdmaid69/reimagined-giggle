import shutil
def move_file(src, dst):
        shutil.move(src, dst)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()