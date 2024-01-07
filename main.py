  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets