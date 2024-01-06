  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)