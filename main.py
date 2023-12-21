import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)