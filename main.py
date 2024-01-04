import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
import json
print(json.dumps({"name": "John", "age": 30}))