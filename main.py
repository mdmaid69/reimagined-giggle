  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread