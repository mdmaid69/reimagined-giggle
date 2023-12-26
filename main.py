  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array