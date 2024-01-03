  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
sentence = "Hello, world!"
from collections import Counter
print("Word frequencies:", Counter(sentence.split()))