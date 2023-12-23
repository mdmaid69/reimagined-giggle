  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())