import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)