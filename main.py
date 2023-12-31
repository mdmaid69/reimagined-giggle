  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])