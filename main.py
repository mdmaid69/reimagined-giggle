  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()