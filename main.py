import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"