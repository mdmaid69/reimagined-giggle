  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()