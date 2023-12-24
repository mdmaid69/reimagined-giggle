  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2