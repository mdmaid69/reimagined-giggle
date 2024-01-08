  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import sklearn.datasets
print(sklearn.datasets.load_iris())