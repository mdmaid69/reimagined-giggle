  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue