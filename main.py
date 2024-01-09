  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)