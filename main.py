  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"