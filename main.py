import math
def calculate_hyperbolic_arc_cosine(x):
        return math.acosh(x)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"