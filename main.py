  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"