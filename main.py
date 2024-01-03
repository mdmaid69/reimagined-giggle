import array
def get_array_as_bytearray(array):
        return bytearray(array)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()