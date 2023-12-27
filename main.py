import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()