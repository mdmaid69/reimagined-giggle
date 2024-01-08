text = "Hello, world!"
print("Words:", len(text.split()))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()