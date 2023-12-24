import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"