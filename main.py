  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}