import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()