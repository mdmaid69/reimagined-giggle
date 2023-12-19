  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)