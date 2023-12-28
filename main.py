  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"
import json
def read_from_json(json_string):
        return json.loads(json_string)