def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()