  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)