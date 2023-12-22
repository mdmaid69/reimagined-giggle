  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  import matplotlib.pyplot as plt
  def plot_pie_chart(labels, sizes):
        plt.pie(sizes, labels=labels)
        plt.show()