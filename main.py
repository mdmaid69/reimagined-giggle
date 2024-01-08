import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size