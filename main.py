  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"