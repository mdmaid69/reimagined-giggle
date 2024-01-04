  import json
  def convert_json_to_dict(json_str):
        return json.loads(json_str)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)