  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)