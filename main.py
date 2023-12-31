import json
def save_json(data, filename):
        with open(filename, "w") as f:
        json.dump(data, f)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)