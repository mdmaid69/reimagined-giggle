  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"