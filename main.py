import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"