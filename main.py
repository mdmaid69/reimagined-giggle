import array
def pop_from_array(array, i=-1):
        return array.pop(i)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"