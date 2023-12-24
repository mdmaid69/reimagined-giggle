  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)