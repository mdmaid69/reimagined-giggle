def calculate_area(radius):
        return 3.14 * radius * radius
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"