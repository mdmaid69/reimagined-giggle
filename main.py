import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"