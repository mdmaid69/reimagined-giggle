  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time