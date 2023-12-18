import array
def get_array_buffer_info(array):
        return array.buffer_info()
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"