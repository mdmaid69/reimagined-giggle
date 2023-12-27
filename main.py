import urllib.request
def download_file(url, filename):
        urllib.request.urlretrieve(url, filename)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value