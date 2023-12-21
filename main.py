import datetime
def get_current_datetime():
        return datetime.datetime.now()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()