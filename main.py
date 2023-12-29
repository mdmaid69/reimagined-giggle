  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import pandas as pd
  def read_excel_file(file_name):
        return pd.read_excel(file_name)