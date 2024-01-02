import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  def convert_to_binary(n):
        return bin(n)