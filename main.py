import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"