  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
n = 10
print("Powers of 2:", [2**x for x in range(n)])