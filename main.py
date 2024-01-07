numbers = [1, 2, 3, 4, 5]
print("Max:", max(numbers))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"