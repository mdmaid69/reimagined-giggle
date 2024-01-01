  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"