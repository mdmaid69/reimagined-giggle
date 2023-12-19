  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import sklearn.datasets
print(sklearn.datasets.load_iris())