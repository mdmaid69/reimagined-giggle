  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import sklearn.datasets
print(sklearn.datasets.load_iris())