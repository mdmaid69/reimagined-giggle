  import random
  def generate_random_number(start, end):
        return random.randint(start, end)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()