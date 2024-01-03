  import matplotlib.pyplot as plt
  def plot_bar_graph(x, y):
        plt.bar(x, y)
        plt.show()
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread