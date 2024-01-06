import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  def calculate_perimeter_triangle(a, b, c):
        return a + b + c