import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"