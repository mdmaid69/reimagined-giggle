  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
def find_difference(list1, list2):
        return set(list1) - set(list2)