  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
def find_frequency(sentence):
        from collections import Counter
        return Counter(sentence.split())