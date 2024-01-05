  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  def calculate_area_triangle(b, h):
        return 0.5 * b * h