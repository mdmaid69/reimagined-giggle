  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"