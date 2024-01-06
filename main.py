  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"