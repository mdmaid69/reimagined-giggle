  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)