import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import json
  def convert_dict_to_json(d):
        return json.dumps(d)