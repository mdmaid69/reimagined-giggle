  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()