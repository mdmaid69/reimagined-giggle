n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"