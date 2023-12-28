  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)