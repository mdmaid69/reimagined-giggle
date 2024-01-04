import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)