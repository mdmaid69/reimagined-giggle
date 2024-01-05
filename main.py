def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()