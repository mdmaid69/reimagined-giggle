sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()