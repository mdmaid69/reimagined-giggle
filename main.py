  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
  import sqlite3
  def close_database_connection(connection):
        connection.close()