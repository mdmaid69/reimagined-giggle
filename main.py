import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"