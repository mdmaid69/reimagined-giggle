  def convert_to_hex(n):
        return hex(n)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)