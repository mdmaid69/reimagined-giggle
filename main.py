  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)