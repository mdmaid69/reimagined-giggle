  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)