  import sys
  def get_python_version():
        return sys.version
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)