  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))