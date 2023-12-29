  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import random
def generate_random_number(start, end):
        return random.randint(start, end)