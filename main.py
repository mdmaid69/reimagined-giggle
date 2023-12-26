import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()