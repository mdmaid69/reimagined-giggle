  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import csv
def write_csv_file(filename, data):
        with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)