  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b