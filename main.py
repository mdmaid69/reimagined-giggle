  def convert_to_octal(n):
        return oct(n)
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)