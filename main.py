  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()