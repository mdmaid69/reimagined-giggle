  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"