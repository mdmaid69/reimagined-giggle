import array
def get_array_itemsize(array):
        return array.itemsize
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"