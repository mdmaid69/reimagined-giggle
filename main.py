  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()