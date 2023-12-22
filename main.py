import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()