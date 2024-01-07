import sklearn.datasets
print(sklearn.datasets.load_iris())
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]