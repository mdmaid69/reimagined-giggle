import math
def calculate_inverse_hyperbolic_tangent(x):
        return math.atanh(x)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"