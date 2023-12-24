import math
def calculate_radians_to_degrees(radians):
        return math.degrees(radians)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"