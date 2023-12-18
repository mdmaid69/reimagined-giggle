import sklearn.datasets
print(sklearn.datasets.load_iris())
import os
def get_environment_variable(var):
        return os.getenv(var)