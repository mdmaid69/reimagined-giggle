import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()