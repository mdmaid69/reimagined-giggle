  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())