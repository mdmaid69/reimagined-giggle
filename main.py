  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True