  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import sklearn.datasets
print(sklearn.datasets.load_iris())