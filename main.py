  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list