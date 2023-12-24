def calculate_average(lst):
        return sum(lst) / len(lst)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()