  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2