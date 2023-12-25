import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"