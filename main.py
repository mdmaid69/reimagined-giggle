  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())