  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)