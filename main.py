import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import json
def read_from_json(json_string):
        return json.loads(json_string)