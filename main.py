  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()