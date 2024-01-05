import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()