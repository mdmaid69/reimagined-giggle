  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())