  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding