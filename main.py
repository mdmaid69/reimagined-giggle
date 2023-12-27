  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
  import sqlite3
  def close_database_connection(connection):
        connection.close()