import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
c.execute("""CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)""")
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()