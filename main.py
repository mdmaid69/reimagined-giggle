  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)