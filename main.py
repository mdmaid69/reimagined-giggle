  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)
  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()