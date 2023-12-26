  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)