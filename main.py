n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()