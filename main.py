  import numpy as np
  def calculate_mean(arr):
        return np.mean(arr)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"