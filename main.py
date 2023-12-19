  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import sklearn.datasets
print(sklearn.datasets.load_iris())