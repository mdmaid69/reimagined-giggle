import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"