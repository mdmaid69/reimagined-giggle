  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)