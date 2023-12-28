  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())