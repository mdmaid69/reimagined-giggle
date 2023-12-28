import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)