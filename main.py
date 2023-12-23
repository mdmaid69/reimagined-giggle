import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import json
def pretty_print_json(data):
        return json.dumps(data, indent=4)