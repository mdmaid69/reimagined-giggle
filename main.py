  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def calculate_average(numbers):
        return sum(numbers) / len(numbers)