import random
def generate_random_sample(population, k):
        return random.sample(population, k)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"