import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"