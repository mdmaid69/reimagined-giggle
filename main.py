  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import sklearn.datasets
print(sklearn.datasets.load_iris())