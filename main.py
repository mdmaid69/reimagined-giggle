  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)