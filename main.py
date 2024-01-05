import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"