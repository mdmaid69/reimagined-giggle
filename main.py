  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import random
def generate_random_sample(population, k):
        return random.sample(population, k)