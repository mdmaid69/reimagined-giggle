import json
def convert_to_json(data):
        return json.dumps(data)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)