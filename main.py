import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()