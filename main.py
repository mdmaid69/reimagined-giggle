import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"