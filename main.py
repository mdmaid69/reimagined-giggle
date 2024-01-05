  import sqlite3
  def close_database_connection(connection):
        connection.close()
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()