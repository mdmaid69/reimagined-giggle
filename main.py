import random
def generate_random_number(start, end):
        return random.randint(start, end)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()