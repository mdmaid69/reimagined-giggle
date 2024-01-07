  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def find_unique_words(sentence):
        return set(sentence.split())