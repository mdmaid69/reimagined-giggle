  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2