import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import sys
  def get_python_version():
        return sys.version