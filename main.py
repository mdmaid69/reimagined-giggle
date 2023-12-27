  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)