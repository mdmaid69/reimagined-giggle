  import json
  def convert_dict_to_json(d):
        return json.dumps(d)
  import requests
  def get_web_page(url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else "Unable to fetch web page"