import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()