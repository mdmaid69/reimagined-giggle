import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"