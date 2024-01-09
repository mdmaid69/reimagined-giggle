def calculate_roi(gain, cost):
        return (gain - cost) / cost
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()