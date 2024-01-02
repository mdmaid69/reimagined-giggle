  def divide_numbers(x, y):
        return x / y if y != 0 else "Cannot divide by zero"
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)