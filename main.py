def find_common_elements(list1, list2):
        return set(list1) & set(list2)
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()