  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)