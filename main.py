  import matplotlib.pyplot as plt
  def plot_graph(x, y):
        plt.plot(x, y)
        plt.show()
def is_palindrome(s):
        return s == s[::-1]