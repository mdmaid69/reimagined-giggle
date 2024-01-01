import array
def set_array_slice(array, i, j, iterable):
        array[i:j] = iterable
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"