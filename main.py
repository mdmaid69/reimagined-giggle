n = 10
print("Square numbers:", [x**2 for x in range(n)])
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"