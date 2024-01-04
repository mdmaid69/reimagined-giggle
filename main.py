  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"