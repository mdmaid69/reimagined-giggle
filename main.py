  import os
  def get_base_name(path):
        return os.path.basename(path)
import sklearn.datasets
print(sklearn.datasets.load_iris())