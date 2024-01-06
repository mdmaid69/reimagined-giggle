import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import json
def load_json(filename):
        with open(filename, "r") as f:
        return json.load(f)