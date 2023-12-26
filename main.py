def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()