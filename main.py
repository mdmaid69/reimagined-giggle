  import matplotlib.pyplot as plt
  def plot_scatter_graph(x, y):
        plt.scatter(x, y)
        plt.show()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()