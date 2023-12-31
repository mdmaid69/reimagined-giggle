  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import sklearn.datasets
print(sklearn.datasets.load_iris())