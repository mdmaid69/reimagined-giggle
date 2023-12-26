import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import matplotlib.pyplot as plt
  def plot_histogram(data, bins):
        plt.hist(data, bins=bins)
        plt.show()