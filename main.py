  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())