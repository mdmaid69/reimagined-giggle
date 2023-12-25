  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)