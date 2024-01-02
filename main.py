import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)