import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare