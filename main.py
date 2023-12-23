import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()