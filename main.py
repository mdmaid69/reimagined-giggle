  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
text = "Hello, world!"
print("Is palindrome:", text == text[::-1])