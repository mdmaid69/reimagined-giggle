  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)