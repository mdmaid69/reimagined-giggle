  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))