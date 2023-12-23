def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"