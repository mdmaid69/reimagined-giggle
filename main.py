text = "Hello, world!"
print("Is palindrome:", text == text[::-1])
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()