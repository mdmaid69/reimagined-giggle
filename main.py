  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c