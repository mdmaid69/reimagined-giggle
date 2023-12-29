import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode