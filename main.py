import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()