  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)