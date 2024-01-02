  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"