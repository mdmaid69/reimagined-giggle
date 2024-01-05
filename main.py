import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"