import math
def calculate_logarithm_base_e(x):
        return math.log(x)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"