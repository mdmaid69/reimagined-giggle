def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"