  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)