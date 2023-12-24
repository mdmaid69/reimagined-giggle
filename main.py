  def is_prime(n):
        for i in range(2, int(n**0.5) + 1):
          if n % i == 0:
        return False
        return True
import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)