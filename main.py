  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))