  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")