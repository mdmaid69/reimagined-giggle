  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()