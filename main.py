import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)