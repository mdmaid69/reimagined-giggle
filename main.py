  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import sklearn.datasets
print(sklearn.datasets.load_iris())