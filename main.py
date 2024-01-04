import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"