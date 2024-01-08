  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()