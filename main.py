import pandas as pd
print(pd.DataFrame({"A": [1, 2], "B": [3, 4]}))
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()