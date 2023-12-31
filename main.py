  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)