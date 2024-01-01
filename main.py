import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"