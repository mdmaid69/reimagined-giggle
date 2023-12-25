  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())