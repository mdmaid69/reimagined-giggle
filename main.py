  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()