  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import sqlite3
  def connect_to_database(db_name):
        return sqlite3.connect(db_name)