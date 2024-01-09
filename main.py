  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)