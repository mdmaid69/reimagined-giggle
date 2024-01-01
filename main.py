import array
def get_array_slice(array, i, j):
        return array[i:j]
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"