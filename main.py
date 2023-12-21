  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)