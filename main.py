  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
sentence = "Hello, world!"
print("Unique words:", len(set(sentence.split())))