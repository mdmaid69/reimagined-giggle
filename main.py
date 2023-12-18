import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()