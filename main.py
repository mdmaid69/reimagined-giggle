  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list