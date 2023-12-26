def calculate_energy(mass, c=3*10**8):
        return mass * c**2
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()