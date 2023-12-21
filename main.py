import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"