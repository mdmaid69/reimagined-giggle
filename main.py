import array
def get_array_as_memoryview(array):
        return memoryview(array)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()