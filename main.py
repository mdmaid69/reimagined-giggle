  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import sklearn.datasets
print(sklearn.datasets.load_iris())