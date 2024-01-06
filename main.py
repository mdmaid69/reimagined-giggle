def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()