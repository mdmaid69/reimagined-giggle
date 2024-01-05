import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"