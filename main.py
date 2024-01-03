import random
def generate_random_choice(choices):
        return random.choice(choices)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()