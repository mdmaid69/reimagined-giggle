import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()