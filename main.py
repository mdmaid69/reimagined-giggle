  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))