def calculate_circumference_circle(r):
        return 2 * 3.14 * r
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"