def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"