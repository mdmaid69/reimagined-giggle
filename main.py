  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()